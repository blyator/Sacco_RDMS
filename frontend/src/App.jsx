import React, { useState, useEffect } from 'react';
import toast, { Toaster } from 'react-hot-toast';
import { Users, PiggyBank, Terminal, CreditCard } from 'lucide-react';
import './App.css';

// Components
import Sidebar from './components/Sidebar';
import TopBar from './components/TopBar';
import Dashboard from './components/Dashboard';
import Members from './components/Members';
import Accounts from './components/Accounts';
import SqlTerminal from './components/SqlTerminal';
import Logs from './components/Logs';


const API_BASE = import.meta.env.VITE_API_BASE

function App() {
  const [activeTab, setActiveTab] = useState('DASHBOARD');
  const [members, setMembers] = useState([]);
  const [accounts, setAccounts] = useState([]);
  const [logs, setLogs] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  // Forms
  const [memberForm, setMemberForm] = useState({ member_id: '', name: '', national_id: '' });
  const [accountForm, setAccountForm] = useState({ account_id: '', member_id: '', balance: '' });
  
  // SQL
  const [sqlQuery, setSqlQuery] = useState('');
  const [sqlResult, setSqlResult] = useState(null);

  const fetchData = async () => {
    setIsLoading(true);
    try {
      const [mRes, aRes] = await Promise.all([
        fetch(`${API_BASE}/members`),
        fetch(`${API_BASE}/accounts`)
      ]);
      if (mRes.ok) setMembers(await mRes.json());
      if (aRes.ok) setAccounts(await aRes.json());
    } catch (error) {
      toast.error('Failed to load data');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => { fetchData(); }, []);

  const addLog = (type, message) => {
    setLogs(prev => [{ id: Date.now(), timestamp: new Date().toLocaleTimeString(), type, message }, ...prev]);
  };

  const handleCreateMember = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_BASE}/members`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          member_id: parseInt(memberForm.member_id),
          name: memberForm.name,
          national_id: memberForm.national_id
        })
      });
      const data = await res.json();
      if (res.ok) {
        toast.success('Member registered successfully!');
        addLog('ACTION', `Added: ${memberForm.name}`);
        setMemberForm({ member_id: '', name: '', national_id: '' });
        fetchData();
      } else {
        toast.error(data.message || 'Failed to register member');
      }
    } catch (err) {
      toast.error(err.message);
    }
  };

  const handleCreateAccount = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`${API_BASE}/accounts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          account_id: parseInt(accountForm.account_id),
          member_id: parseInt(accountForm.member_id),
          balance: parseInt(accountForm.balance)
        })
      });
      const data = await res.json();
      if (res.ok) {
        toast.success('Account opened successfully!');
        addLog('ACTION', `Opened: #${accountForm.account_id}`);
        setAccountForm({ account_id: '', member_id: '', balance: '' });
        fetchData();
      } else {
        toast.error(data.message || 'Failed to open account');
      }
    } catch (err) {
      toast.error(err.message);
    }
  };

  const handleExecuteSQL = async () => {
    if (!sqlQuery.trim()) return;
    setSqlResult({ status: 'loading', data: 'Executing...' });
    try {
      const res = await fetch(`${API_BASE}/sql`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: sqlQuery })
      });
      const data = await res.json();
      if (res.ok) {
        setSqlResult({ status: 'success', data: data });
        addLog('SQL', `Executed: ${sqlQuery}`);
        toast.success('Query executed successfully');
        if (sqlQuery.toUpperCase().includes('INSERT') || sqlQuery.toUpperCase().includes('UPDATE') || sqlQuery.toUpperCase().includes('DELETE')) {
           fetchData();
        }
      } else {
        setSqlResult({ status: 'error', data: data.message });
        addLog('SQL_ERR', data.message);
        toast.error('SQL Execution Failed');
      }
    } catch (err) {
      setSqlResult({ status: 'error', data: err.message });
      toast.error(err.message);
    }
  };

  const totalFunds = accounts.reduce((acc, curr) => acc + (curr.balance || 0), 0);

  const statCards = [
    {
      title: "Total Members",
      value: members.length,
      icon: Users,
      description: "Active registered members",
      color: "text-accent",
    },
    {
      title: "Active Accounts",
      value: accounts.length,
      icon: CreditCard,
      description: "Savings accounts opened",
      color: "text-accent",
    },
    {
      title: "Total Holdings",
      value: `Kes ${totalFunds.toLocaleString()}`,
      icon: PiggyBank,
      description: "Total Sacco revenue",
      color: "text-accent",
    },
    {
      title: "System Logs",
      value: logs.length,
      icon: Terminal,
      description: "Recorded activities",
      color: "text-accent",
    },
  ];

  return (
    <div className="flex h-screen bg-base-200 text-base-content font-sans overflow-hidden">
      
      <Toaster position="top-right" reverseOrder={false} />
      
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />


      <main className="flex-1 flex flex-col overflow-hidden relative">
        
        <TopBar 
          activeTab={activeTab} 
          fetchData={fetchData} 
          isLoading={isLoading} 
        />


        <div className="flex-1 overflow-auto p-8">
          
          {activeTab === 'DASHBOARD' && (
            <Dashboard 
              statCards={statCards} 
              members={members} 
              logs={logs} 
              fetchData={fetchData} 
            />
          )}

          {activeTab === 'MEMBERS' && (
            <Members 
              members={members} 
              memberForm={memberForm} 
              setMemberForm={setMemberForm} 
              handleCreateMember={handleCreateMember} 
            />
          )}

          {activeTab === 'ACCOUNTS' && (
            <Accounts 
              accounts={accounts} 
              accountForm={accountForm} 
              setAccountForm={setAccountForm} 
              handleCreateAccount={handleCreateAccount} 
            />
          )}

          {activeTab === 'SQL' && (
            <SqlTerminal 
              sqlQuery={sqlQuery} 
              setSqlQuery={setSqlQuery} 
              sqlResult={sqlResult} 
              handleExecuteSQL={handleExecuteSQL} 
            />
          )}

          {activeTab === 'LOGS' && (
            <Logs logs={logs} />
          )}

        </div>
      </main>
    </div>
  );
}

export default App;