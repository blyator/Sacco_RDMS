import React from 'react';
import { UserPlus } from 'lucide-react';

const Members = ({ members, memberForm, setMemberForm, handleCreateMember }) => {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 animate-fade-in pb-10">
      {/* Registration Form - Left Column */}
      <div className="lg:col-span-1">
         <div className="card bg-base-100 shadow-xl border border-base-200 sticky top-0">
            <div className="card-body">
               <h3 className="card-title text-lg font-black uppercase mb-4 flex items-center gap-2">
                   <UserPlus className="w-6 h-6 text-primary" /> New Member
               </h3>
               <form onSubmit={handleCreateMember} className="flex flex-col gap-4">
                  <div className="form-control w-full">
                     <label className="label"><span className="label-text font-bold text-xs uppercase opacity-60">Member ID</span></label>
                     <input type="number" className="input input-bordered w-full bg-base-200" value={memberForm.member_id} onChange={e => setMemberForm({...memberForm, member_id: e.target.value})} required />
                  </div>
                  <div className="form-control w-full">
                     <label className="label"><span className="label-text font-bold text-xs uppercase opacity-60">Full Name</span></label>
                     <input type="text" className="input input-bordered w-full bg-base-200" value={memberForm.name} onChange={e => setMemberForm({...memberForm, name: e.target.value})} required />
                  </div>
                  <div className="form-control w-full">
                     <label className="label"><span className="label-text font-bold text-xs uppercase opacity-60">National ID</span></label>
                     <input type="text" className="input input-bordered w-full bg-base-200" value={memberForm.national_id} onChange={e => setMemberForm({...memberForm, national_id: e.target.value})} required />
                  </div>
                  <button type="submit" className="btn btn-primary w-full mt-4 font-black tracking-widest">Register</button>
               </form>
            </div>
         </div>
      </div>

      {/* Members Table - Right Column */}
      <div className="lg:col-span-2">
         <div className="card bg-base-100 shadow-xl border border-base-200 h-full">
            <div className="card-body p-0">
               <div className="p-4 border-b border-base-200 flex items-center justify-between bg-base-200/30">
                  <h2 className="card-title text-base font-black uppercase tracking-tight">Member Directory</h2>
                  <div className="badge badge-primary badge-outline">{members.length} Total</div>
               </div>
               <div className="overflow-x-auto">
                  <table className="table table-zebra w-full">
                     <thead className="bg-base-200/50 text-xs font-black uppercase opacity-60">
                        <tr>
                           <th>ID</th>
                           <th>Full Name</th>
                           <th>National ID</th>
                        </tr>
                     </thead>
                     <tbody>
                        {members.map(m => (
                          <tr key={m.member_id}>
                             <th className="font-mono text-primary">#{m.member_id}</th>
                             <td className="font-bold uppercase">{m.name}</td>
                             <td className="opacity-70">{m.national_id}</td>
                          </tr>
                        ))}
                        {members.length === 0 && <tr><td colSpan="3" className="text-center py-8 opacity-50">No records found</td></tr>}
                     </tbody>
                  </table>
               </div>
            </div>
         </div>
      </div>
    </div>
  );
};

export default Members;